import React, ***REMOVED***Component***REMOVED*** from 'react';
import Header from "./Header";


export default class Template extends Component ***REMOVED***
	state = ***REMOVED***
		update: false
	***REMOVED***

	refreshHome()***REMOVED***
		this.setState(***REMOVED***update: !this.state.update***REMOVED***);
	***REMOVED***

	render()***REMOVED***
		let props = this.props;
		return (
			<div>
				<Header refreshHome=***REMOVED***this.refreshHome***REMOVED*** />
				***REMOVED***React.cloneElement(props.component, props=***REMOVED***props***REMOVED***)***REMOVED***
			</div>
		)
	***REMOVED***
***REMOVED***
