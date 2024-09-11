import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import VideoUpload from './components/VideoUpload';

function App() {
  const [data, setData] = useState([]);

  const fetchData = async (filename) => {
    try {
      const response = await axios.post('http://localhost:5000/detect', { video_path: filename });
      setData(response.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const totalVehicles = data.reduce((acc, frame) => acc + frame.vehicle_count, 0);
  const totalCars = data.reduce((acc, frame) => acc + frame.car_count, 0);
  const totalMotorcycles = data.reduce((acc, frame) => acc + frame.motorcycle_count, 0);
  const totalBuses = data.reduce((acc, frame) => acc + frame.bus_count, 0);
  const totalTrucks = data.reduce((acc, frame) => acc + frame.truck_count, 0);

  return (
    <div className="App">
      <h1>Vehicle Detection Dashboard</h1>
      <VideoUpload onUpload={fetchData} />
      {data.length > 0 && (
        <div className="metrics">
          <h2>Total Vehicles Detected: {totalVehicles}</h2>
          <h3>Car Count: {totalCars}</h3>
          <h3>Motorcycle Count: {totalMotorcycles}</h3>
          <h3>Bus Count: {totalBuses}</h3>
          <h3>Truck Count: {totalTrucks}</h3>
        </div>
      )}
    </div>
  );
}

export default App;
