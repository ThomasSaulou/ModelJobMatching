import { Button } from 'element-ui';
import Vue from 'vue';

Vue.component(Button.name, Button);


export default {
	data () {
		return {
			name: 'Home',
			isCollapse: false,
			index:1,
			activeItemIdx:1,
		}
	}
}