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
			candidateName:null,
			candidateId:null,
			jobList:[],	
			jobs:'',
			RIASEC: {
				R: 0,
				I: 0,
				A: 0,
				S: 0,
				E: 0,
				C: 0
				}
			}
		},
	
	methods: {
		addjob(){
			this.jobList.push({'jobCode':0,'score':0})
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

		sendCandidateToBdd(){
			let data={
				'name':this.candidateName,
				'ID':this.candidateId,
				'listJobScore':this.jobList,
				'RIASEC':this.RIASEC
			}
			console.log('ok')
			fetch('http://127.0.0.1:5000/createcandidate',{
			method: 'POST', 
			headers:{"Content-Type":"application/json"},
			body: JSON.stringify(data),
			})
			.catch(error =>{
				console.log(error)
			});
		}
	},

	mounted() {
		this.getAllJobs()
	},
}