<template>
  <div class="content-container">
    <div class="column is-10">
      <div class="section content-title-group">
        <h2 class="title">Problems</h2>
        <ul>
          <li v-for="problem in problems" :key="problem.id">
            <div class="card">
              <div class="card-content">
                <div class="content">
                  <div :key="problem.name" class="name">
                    #{{ problem.id }} - {{ problem.name }} <label class="solved" v-if="problem.solved" > Solved! </label>
                  </div>
                </div>
              </div>
              <footer class="card-footer">
                <router-link
                  tag="button"
                  class="link card-footer-item"
                  :to="{ name: 'problem-detail', params: { id: problem.id } }"
                >
                  <i class="fas fa-check"></i>
                  <span>Details</span>
                </router-link>
              </footer>
            </div>
          </li>
        </ul>
      </div>
      <div class="notification is-info" v-show="message">{{ message }}</div>
    </div>
  </div>
</template>

<script>

import { dataService } from '../shared/data.service';

export default {
  name: 'Problems', 
  data() {
    return{
      problems: [], 
      solutions: [], 
      message: ''
    };
  }, 
  async created() {
    await this.loadProblems();
    await this.loadSolutions();
  }, 
  methods: {
    async loadProblems() {
      this.problems = [];
      this.message = 'Loading Problems, please wait...';
      this.problems = await dataService.getProblems();
      this.message = '';
    },
    async loadSolutions() {
      this.solutions = [];
      this.message = 'Loading Solutions, please wait...';
      this.solutions = await dataService.getSolutions();
      this.message = '';
    }
  }
};
</script>
