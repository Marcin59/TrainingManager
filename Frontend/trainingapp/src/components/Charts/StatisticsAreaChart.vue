<script>
import { Line } from "vue-chartjs";
import {getStatistics} from "@/services/statisticServise.js"
import moment from 'moment'

export default {
  extends: Line,
  data() {
    return {
        chartData: {},
    };
  },
  async mounted() {
    await this.updateData()
    this.renderChart(
      this.chartData,
      { responsive: true, 
      maintainAspectRatio: false,
      scales: {
        xAxes: [{
            type: 'time',
            time: { parser: 'YYYY/MM/DD HH:mm:ss' },
            scaleLabel: {
                        display:     true,
                        labelString: 'Date'
                },
            ticks: {
                    // Include a dollar sign in the ticks
                    callback: function(values) {
                        return values;
                    }
                }
          }],
        }
      }
    );
  },
    methods: {
      async updateData() {
          var datasets = []
          this.dataFromServer = await getStatistics()
          for (var key in this.dataFromServer) {
            var newDataset = {}
            newDataset['label'] = key
            newDataset['data'] = []
            this.dataFromServer[key].forEach(element => {
                newDataset['data'].push({x: moment.utc(element.date).format('YYYY/MM/DD HH:mm:ss'), y: element.weight})
            });
            datasets.push(newDataset)
            }
          this.chartData['datasets'] = datasets
      },
  }
};
</script>