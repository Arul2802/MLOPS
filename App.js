import React from 'react';
import './App.css'; // Import CSS file for styling

const InputForm = () => {
    return (
      <div style={{ textAlign: 'center' }}>
      <div className='inputbox'>
        <h2>GDP PER CAPITA PREDICTION</h2>
        <p>Overall_rank</p>
        <input
          type="text"
          name="input1"
          placeholder="Enter the rank"
        /><br/>
        <p>Score</p>
        <input
          type="text"
          name="input2"
          placeholder="Enter the score"
        /><br/>
        <p>Social_support</p>
        <input
          type="text"
          name="input3"
          placeholder="Enter the value"
        /><br/>
        <p>Healthy_life_expectancy</p>
        <input
          type="text"
          name="input4"
          placeholder="Enter the value"
        /><br/>
        <p>Freedom_to_make_life_choices</p>
        <input
          type="text"
          name="input5"
          placeholder="Enter the value"
        /><br/>
        <p>Generosity</p>
        <input
          type="text"
          name="input6"
          placeholder="Enter the value"
        /><br/>
        <p>Perceptions_of_corruption</p>
        <input
          type="text"
          name="input7"
          placeholder="Enter the value"
        /><br/>
      </div><br/>
      <button >Predict</button>
    </div>

    );
}

export default InputForm;

