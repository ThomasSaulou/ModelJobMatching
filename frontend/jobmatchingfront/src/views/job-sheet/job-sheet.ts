import { Button, Select } from 'element-ui';
import Vue from 'vue';
import Navbar from '../../components/navbar/navbar.vue';
import { Bar } from 'vue-chartjs';
import BarChart from './BarChart.js'


Vue.component(Button.name, Button);
Vue.component(Select.name, Select);



export default {
	extends: Bar,
	components:{
		Navbar,
		BarChart,
	},
	data () {
		return {
			jobs:[],
			jobSheet:'test',
			objetRiasec:{'R':0,'I':0,'A':0,'S':0,'E':0,'C':0},
			datacollection: null,
			keySkills:[],
			code:0,
		}
	},

	
	methods: {
		compare(a, b) {
			return  b.frequency-a.frequency;
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

		getKeySkills(){
			let skills=this.jobSheet.competencesDeBase
			let listKeySkills=[]
			skills.forEach(skill => {
				if(skill.competenceCle ===true){
					listKeySkills.push({
						'name':skill.libelle,
						'frequency':skill.frequence
					})
				}
			});
			this.keySkills=listKeySkills.sort(this.compare)

		},

		fillData() {
			this.datacollection = {
				labels: ['R','I','A','S','E','C'],
					datasets: [
						{
						label: 'RIASEC',
						backgroundColor: '#087979',
						data: [this.objetRiasec.R,this.objetRiasec.I,this.objetRiasec.A,this.objetRiasec.S,this.objetRiasec.E,this.objetRiasec.C]

						}, 
					]
				}
		},
		
		
		async getJobSheet(code){
			await fetch(`http://127.0.0.1:5000/job/${code}`,{
		method: 'GET', 
		headers:{"Content-Type":"application/json"}
		})
		.then(resp=>resp.json())
		.then(data=> {this.jobSheet=data})
		.catch(error =>{
			console.log(error)
		});
		this.perCentRiasecSkills()
		this.getKeySkills()
		},

		perCentRiasecSkills(){

			let skills=this.jobSheet.competencesDeBase
			this.objetRiasec={'R':0,'I':0,'A':0,'S':0,'E':0,'C':0}
			skills.forEach(skill => {
				if(skill.typeCompetence ==="SavoirFaire"){
					this.objetRiasec[skill['riasecMajeur']]+=1
				}
			});
			this.fillData()
			
		}
		

	},

	mounted() {
		// if you want to call it on component mounted
		this.getAllJobs()
		this.getJobSheet('G1702')
		this.fillData()
	},
}