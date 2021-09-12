import { Button, Select } from 'element-ui';
import Vue from 'vue';
import Navbar from '../../components/navbar/navbar.vue';
import Matching from '../../components/candidate-job-match/candidate-job-match.vue';
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
		Matching,
	},
	data () {
		return {
			


			candidates:null,
			jobs:null,
			candidateId:null,
			missionCode:null,
			matchingResult:null,
			isMatchLoaded:false,
			domaines:[],
			name:"TOTO",
			tableDataJobs:  [ {
				jobExperience: 'Same Job',
				amount: '4',
				score: '70%'
				}, {
				jobExperience: 'Similar Job',
				amount: '3',
				score: '40%'
				},],
			tableDataSkills:  [ 
				{
				skillExperience: 'Soft Skills',
				amount: '-',
				score: '70%'
				},
				{
				skillExperience: 'Key Skills',
				amount: '4/6',
				score: '60%'
				}, {
				skillExperience: 'Basic Skills',
				amount: '3/10',
				score: '40%'
				},
				{
				skillExperience: 'Similar Skills',
				amount: '8/14',
				score: '50%'
				}],
			tableDataRIASEC:  [ {
				RIASEC: 'Job Majeur',
				riasecScore: '70%',
				}, {
				RIASEC: 'Job Mineur',
				riasecScore: '90%',
				},
				{
				RIASEC: 'Skills Riasec',
				riasecScore: '80%',
				}],
			tableDataEmotion:  [ {
				happy: '60%',
				neutre: '30%',
				sad:'10%'
				}],
			optionsSpiderGraph : {
					series: [
					{
						name: "Personnal RIASEC",
						data: [75, 52, 68, 24, 33, 90]
					},
					],
					labels: ['R', 'I', 'A', 'S', 'E', 'C']
				},
					
				
		}
		},


	
	methods: {
		getAllCandidates()  {
			console.log('bjr')
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
			.then(data=> {this.jobs=data.list;
				this.domaines=this.jobs.map(item => item.domaine)
				.filter((value, index, self) => self.indexOf(value) === index);
				console.log(this.domaines)})
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
			.then(data=> {this.matchingResult=data.result; 
				this.isMatchLoaded=true;
				this.buildDataTables()})
			.catch(error =>{
				console.log(error)
			});
			},
		
		buildDataTables(){
			this.tableDataJobs=this.buildJobTable()
			this.tableDataSkills=this.buildTableDataSkills()
			this.tableDataEmotion=this.buildTableDataEmotion()
			this.tableDataRIASEC=this.buildTableDataRIASEC()
			this.optionsSpiderGraph=this.buildOptionsSpiderGraph()
			this.name=this.candidates.find(candidat=> candidat.id === this.candidateId).name
		},

		buildTableDataSkills(){
			return [ 
				{
				skillExperience: 'Soft Skills',
				amount: '-',
				score: Math.round(this.matchingResult["softSkillScore"]*100)/100
				},
				{
				skillExperience: 'Key Skills',
				amount: `${this.getNbKeySkillDone()}/${this.matchingResult['keySkills'].length}`,
				score: Math.round(this.matchingResult["Skill_Key_AVG_Score"]/this.matchingResult['keySkills'].length * 100) / 100,
				}, {
				skillExperience: 'Basic Skills',
				amount: `${this.matchingResult["skillScore"]["count"]}/${this.matchingResult["skillScore"]["totalSkills"]}`,
				score: Math.round(this.matchingResult["skillScore"]["score"]/this.matchingResult["skillScore"]["count"] * 100) / 100,
				
				},
				{
				skillExperience: 'Similar Skills',
				amount: '-',
				score: '-'
				}]

		},
		getNbKeySkillDone(){
			const keySkills=this.matchingResult['keySkills']
			let count=0;
			keySkills.forEach(skill => {
				if(skill['score']!==0){
					count+=1
				}
			});
			return count
		},

		buildJobTable(){
			
			return  [ {
				jobExperience: 'Same Job',
				amount: this.matchingResult['scoreFromROMEJobs']["nbJob"],
				score: this.round2(this.matchingResult['scoreFromROMEJobs']["score"])
				}, {
				jobExperience: 'Similar Job',
				amount: this.matchingResult['secondDegreeJobScore']["count"],
				score: this.round2(this.matchingResult['secondDegreeJobScore']["score"])
				}]
		},

		buildTableDataRIASEC(){

			return [ {
				RIASEC: 'Job Majeur',
				riasecScore: this.round2(this.matchingResult['RIASEC_majeur']),
				}, {
				RIASEC: 'Job Mineur',
				riasecScore: this.round2(this.matchingResult['RIASEC_mineur']),
				},
				{
				RIASEC: 'Skills Riasec',
				riasecScore: Math.round((this.matchingResult['Skills_Riasec']*100)/100),
				}]
				
		},
		buildTableDataEmotion(){
			return [ {
				happy: this.round2(this.matchingResult['getInterviewScore']['happy']),
				neutre: this.round2(this.matchingResult['getInterviewScore']['neutre']),
				sad:this.round2(this.matchingResult['getInterviewScore']['sad']),
				}]
		},
		round2(number){
			return Math.round((number)*100)/100
		},

		buildOptionsSpiderGraph () {
			const riasec=this.matchingResult["candidateRIASEC"]["RIASEC"]
			return { series: [
			{
				name: "Personnal RIASEC",
				data: [riasec["R"], riasec["I"], riasec["A"], riasec["S"], riasec["E"], riasec["C"]]
			},
			],
			labels: ['R', 'I', 'A', 'S', 'E', 'C']
		}
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
