<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
    };
  },
  mounted() {
    this.renderChart(
      {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July"
        ],
        datasets: [
          {
            label: "Data One",
            borderColor: "#FC2525",
            backgroundColor: "#FC2525",
            data: [40, 39, 10, 40, 39, 80, 40]
          },
          {
            label: "Data Two",
            borderColor: "#05CBE1",
            backgroundColor: "#05CBE1",
            data: [60, 55, 32, 10, 2, 12, 53]
          }
        ]
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>