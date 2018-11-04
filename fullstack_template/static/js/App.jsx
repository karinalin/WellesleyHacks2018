import React from 'react';
 
export default class App extends React.Component {
 
    constructor(props) {
        super(props);
         this.state = { image: "" };
         this.previewFile = this.previewFile.bind(this);
    }
 
    previewFile(event) {
    	if (event.target.files && event.target.files[0]) {
            let reader = new FileReader();
            reader.onload = (e) => {
                this.setState({image: e.target.result});
                console.log(reader.result);
            };
            reader.readAsDataURL(event.target.files[0]);
        }
    };
 
    render() {
        return (
            <div>
            	<input type="file" onChange={this.previewFile} />
            	<img id="target" src={this.state.image} height={200} />
            </div>
        );
    }
}