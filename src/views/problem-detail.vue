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
            <div class="field">
              <label class="label" for="solved">Solved</label>
              <input type="checkbox" name="solved" v-model="problem.solved" />
            </div>
          </div>
        </div>
        <footer class="card-footer">
          <button
            class="link card-footer-item cancel-button"
            @click="cancel()"
          >
            <i class="fas fa-undo"></i>
            <span>Cancel</span>
          </button>
          <button class="link card-footer-item" @click="update()">
            <i class="fas fa-save"></i>
            <span>Save</span>
          </button>
        </footer>
    </div>
  </div>
</template>

<script>

import { dataService } from '../shared/data.service';
import { logger } from '../shared/logger';

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
      solution: {}
    }
  }, 
  async created(){
    this.problem = await dataService.getProblem(this.id);
    if (this.problem != null && this.problem.solved)
      this.solution = await dataService.getSolution(this.problem.id);
  }, 
  methods: {
    cancel() {
      logger.info('problem-detail cancel button pressed');
      this.$router.push({ name: 'problems' });
    }, 
    async update() {
      logger.info('problem-detail update button pressed');
      await dataService.updateProblem(this.problem);
      this.$router.push({ name: 'problems' });
    }
  }
};
</script>


