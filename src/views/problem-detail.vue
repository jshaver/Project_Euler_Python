<template>
  <div class="section content-title-group">
    <h2 class="title">Problem Details</h2>
    <div class="card">
      <header class="card-header">
        <p class="card-header-title">#{{ problem.id }} - {{ problem.name }} </p>
      </header>
      <div class="card-content">
        <div class="content">
          <div class="field">
            <label class="label" for="id">ID</label>
            <label class="input" name="id" readonly>{{ problem.id }}</label>
          </div>
          <div class="field">
            <label class="label" for="name">Problem Name</label>
            <input class="input" name="name" v-model="problem.name" />
          </div>
          <div>
            <a v-bind:href="'http://projecteuler.net/problem='+problem.id" target="_blank">Link to Description</a>
          </div>
          <div class="field">
            <label class="label" for="solved">Solved</label>
            <input type="checkbox" name="solved" v-model="problem.solved" />
          </div>
          <div v-show="problem.solved">
            <label class="label" for="solutionValue">Solution Value</label>
            <input class="input" name="solutionValue" v-model="solution.solutionValue" />
          </div>
          <div v-show="problem.solved">
            <label class="label" for="solutionDateSolved">Date Solved</label>
            <input class="input" type="date" name="solutionDateSolved" v-model="solution.dateSolved" />
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <button class="link card-footer-item cancel-button" @click="cancel()">
          <i class="fas fa-undo"></i>
          <span>Cancel</span>
        </button>
        <button class="link card-footer-item" @click="update()">
          <i class="fas fa-save"></i>
          <span>Save</span>
        </button>
      </footer>
    </div>
    <div>
      <div class="card-content">
        <div class="content">
          <div class="field">
            <label class="label" for="problemInput">Problem Input</label>
            <input class="input" name="problemInput" v-model="problemInput" />
          </div>
          <div class="field">
            <label class="label" for="problemResult">Problem Result</label>
            <input class="input" name="problemResult" v-model="problemResult" readonly/>
          </div>
        </div>
      </div>
      <footer class="card-footer">
        <button class="link card-footer-item" @click="clear()">
          <span>Clear</span>
        </button>
        <button class="link card-footer-item" @click="solve()" >
          <span>Solve</span>
        </button>
      </footer>
    </div>
  </div>
</template>

<script>

import { dataService } from '../services/data.service';
import { pythonService } from '../services/python.service';
import { logger } from '../shared/logger';
import { format } from 'date-fns';

const displayDateFormat = 'MMM DD, YYYY';

export default {
  name: 'ProblemDetail', 
  props: {
    id: {
      type: Number, 
      default: 0
    }
  },
  data(){
    return {
      problem: {}, 
      solution: {}, 
      problemInput: '', 
      problemResult: ''
    };
  }, 
  async created(){
    this.problem = await dataService.getProblem(this.id);
    if (this.problem != null && this.problem.solved)
      this.solution = await dataService.getSolution(this.problem.id);
  }, 
  methods: {
    cancel() {
      this.$router.push({ name: 'problems' });
    }, 
    async update() {
      await dataService.updateProblem(this.problem);
      
      if (this.problem.solved){
        if (this.solution != null && this.solution != {} && this.solution.id != null)
          await dataService.updateSolution(this.solution);
        else if (this.solution != null && this.solution != {} && this.solution.id == null)
          this.solution.id = this.problem.id;
          await dataService.createSolution(this.solution);
      } else if (!this.problem.solved && this.solution != {} && this.solution.id != null) {
        await dataService.deleteSolution(this.solution.id);
      }

      this.$router.push({ name: 'problems' });
    }, 
    clear(){
      this.problemInput = '';
      this.problemResult = '';
    },
    async solve(){
      let result = await pythonService.solveProblem(this.problem.id, this.problemInput);
      if (result > 0)
        this.problemResult = result;
    }
  }, 
  filters: {
    shortDate: function(d) {
      return format(d, displayDateFormat);
    }
  }
};
</script>


