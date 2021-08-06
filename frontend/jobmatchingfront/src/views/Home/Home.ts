import { Button } from 'element-ui';
import Vue from 'vue';
import Navbar from '../../components/navbar/navbar.vue'

Vue.component(Button.name, Button);


export default {
	data () {
		return {
		
		}
	},
	components:{
		Navbar
	},
	methods: {
		getAllMissions()  {
		fetch('http://127.0.0.1:5000/jobs',{
		method: 'GET', 
		headers:{"Content-Type":"application/json"}
		})
		.then(resp=>resp.json())
		.then(data=> console.log(data))
		.catch(error =>{
			console.log(error)
		});
}
	}
}