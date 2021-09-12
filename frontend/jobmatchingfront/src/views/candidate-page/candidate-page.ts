import { Button, Select } from 'element-ui';
import Vue from 'vue';
import Navbar from '../../components/navbar/navbar.vue';
import { Bar } from 'vue-chartjs';
import SpiderGraph from 'vue-spider-graph'
import VueApexCharts from 'vue-apexcharts'
 


Vue.component(Button.name, Button);
Vue.component(Select.name, Select);
Vue.component('apexchart', VueApexCharts)



export default {
	extends: Bar,
	components:{
		Navbar,
		SpiderGraph,
	},
	data () {
		return {
			candidates:'',
			candidate:'',
			id:1,
			objetRiasec:{'R':0,'I':0,'A':0,'S':0,'E':0,'C':0},
			datacollection: null,
			skills:[],
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
		},


	
	methods: {
		getAllCandidates()  {
			fetch('http://127.0.0.1:5000/candidates',{
			method: 'GET', 
			headers:{"Content-Type":"application/json"}
			})
			.then(resp=>resp.json())
			.then(data=> {this.candidates=data.list})
			.catch(error =>{
				console.log(error)
			});
		},
		

		getCandidateByID(id)  {
		console.log('hello')
		console.log(id)
		fetch(`http://127.0.0.1:5000/candidate/${id}`,{
		method: 'GET', 
		headers:{"Content-Type":"application/json"}
		})
		.then(resp=>resp.json())
		.then(data=> {this.candidate=data.result;
			let riasec=this.candidate.RIASEC;
			this.options.series[0].data=[riasec.R,riasec.I,riasec.A,riasec.S,riasec.E,riasec.C]
			let jobRiasec=this.candidate.JobRIASEC;
			this.options.series[1].data=[jobRiasec.R.score,jobRiasec.I.score,jobRiasec.A.score,jobRiasec.S.score,jobRiasec.E.score,jobRiasec.C.score]
			this.skills=this.candidate.skills
			this.updateSeriesLine()
		})
		.catch(error =>{
			console.log(error)
		});
		},

		updateSeriesLine() {
			this.$refs.radarchart.updateSeries([{
				data: this.options.series[0].data,
				}], false, true);
			}

	},

	mounted() {
		// if you want to call it on component mounted
		this.getAllCandidates();
		this.getCandidateByID(1)
		
		// let riasec=this.candidate.RIASEC
		// console.log(riasec)
		// this.options.series.data=[riasec.R,riasec.I,riasec.A,riasec.S,riasec.E,riasec.C]
	},
}