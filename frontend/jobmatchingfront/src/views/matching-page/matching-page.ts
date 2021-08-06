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
			candidates:null,
			jobs:null,
			candidateId:null,
			missionCode:null,
			matchingResult:null,
			isMatchLoaded:false,
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
		getAllJobs()  {
			fetch('http://127.0.0.1:5000/jobs',{
			method: 'GET', 
			headers:{"Content-Type":"application/json"}
			})
			.then(resp=>resp.json())
			.then(data=> {this.jobs=data.list})
			.catch(error =>{
				console.log(error)
			});
			},

		
		getMatchResult(){
			let data={
				'candidateId':this.candidateId,
				'missionCode':this.missionCode,
			}
			fetch('http://127.0.0.1:5000/matching',{
			method: 'POST', 
			headers:{"Content-Type":"application/json"},
			body: JSON.stringify(data),
			})
			.then(resp=>resp.json())
			.then(data=> {this.matchingResult=data.result; this.isMatchLoaded=true;})
			.catch(error =>{
				console.log(error)
			});
			},
		},

	mounted() {
		// if you want to call it on component mounted
		this.getAllCandidates();
		this.getAllJobs();
		// let riasec=this.candidate.RIASEC
		// console.log(riasec)
		// this.options.series.data=[riasec.R,riasec.I,riasec.A,riasec.S,riasec.E,riasec.C]
	},
}