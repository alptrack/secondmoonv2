import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import Collapsible from 'react-collapsible';
import {connect} from 'react-redux';
import {settings} from "../actions";

class Header extends Component {
	state = {
		headerHeight: 0,
		discountDismissed: false,
	}
	componentDidMount() {
		if (!this.props.settings.length){
	    	this.props.fetchSettings();
		}
		let height = this.divElement.clientHeight;
		this.setState({ headerHeight: height });
		window.addEventListener("resize", this.setState({ headerHeight: height }));
	}	

	componentWillUnmount(){
		let height = this.divElement.clientHeight;
		window.removeEventListener("resize", this.setState({ headerHeight: height }));
	}

	dismissAlert() {
		this.setState({discountDismissed: true},()=>{
			const height = this.divElement.clientHeight;
			this.setState({ headerHeight: height });
		})
		
	}



	render(){
			return(
				<div>
					<nav id="header" className="navbar navbar-light fixed-top navbar-expand-lg py-md-0 py-0 m0 p0" ref={ (divElement) => this.divElement = divElement}>
						<div className="container-fluid m0 p0">
							<div className="row m0 p0" style={{width:'100%'}}>
								<div className="col-10 col-md-9">
									<Link to="/" className="nav-brand col-10 col-md-9" onClick={()=>this.props.refreshHome()}>
										<img src="https://i.imgur.com/UEdsoNTm.png"/>
										<h3 className="align-middle header-text">Second Moon Records</h3>
									</Link>
								</div>
								<button className="navbar-toggler" 
										type="button" 
										data-toggle="collapse" 
										data-target="#navbarToggler" 
										aria-controls="navbarToggler" 
										aria-expanded="false" 
										aria-label="Toggle navigation"
								>
									<span className="navbar-toggler-icon"></span>
								</button>
								<div className="collapse navbar-collapse col-3" id="navbarToggler">
									<ul className="navbar-nav">
										<li className="nav-item py-0"><Link to="/contact" className="nav-link">Contact</Link></li>
										<li className="nav-item py-0"><Link to="/tag" className="nav-link">Filter</Link></li>
										<li className="nav-item py-0"><Link to="/about" className="nav-link">About</Link></li>
									</ul>
								</div>
							</div>
						</div>
					</nav>
					<div id="header-spacer" style={{marginBottom: this.state.headerHeight + 50 + 'px'}}></div>
				</div>
			)
	}
}

const mapStateToProps = state => {
	let errors = [];
	if (state.settings.errors) {
		errors = [...errors, Object.keys(state.settings.errors).map(field => {
			return {field, message: state.settings.errors[field]};
		})];
	}
	return {
		settings: state.settings,
		errors
	}
}

const mapDispatchToProps = dispatch => {
	return {
		fetchSettings: () => {
			dispatch(settings.fetchSettings());
	    },
	}
}

export default connect(mapStateToProps, mapDispatchToProps)(Header)
