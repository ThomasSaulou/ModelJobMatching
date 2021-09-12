import VueApexCharts from 'vue-apexcharts'
import Vue from 'vue';

Vue.component('apexchart', VueApexCharts)

export default {
  methods: {
    tableRowClassName({ rowIndex}) {
      if (rowIndex === 1) {
        return 'warning-row';
      } else if (rowIndex === 3) {
        return 'success-row';
      }
      return '';
    }
  },
  props: ['name','tableDataJobs','tableDataSkills','tableDataRiasec','tableDataEmotion',"optionsSpiderGraph"],
  data() {
    return {
      options : {
        series: [
        {
          name: "Perso RIASEC",
          data: [75, 52, 68, 24, 33, 90]
        },
        {
          name: "Job RIASEC",
          data: [45, 72, 38, 54, 33, 60]
        }
        
        ],
        labels: ['R', 'I', 'A', 'S', 'E', 'C']
      },
    }
  }
}