import React, { useState } from 'react';
import axios from 'axios';

const VideoUpload = ({ onUpload }) => {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [videoURL, setVideoURL] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    setUploading(true);

    const formData = new FormData();
    formData.append('video', file);

    try {
      const uploadResponse = await axios.post('http://localhost:5000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      const { filename } = uploadResponse.data;
      const videoURL = `http://localhost:5000/videos/${filename}`;
      setVideoURL(videoURL);
      onUpload(filename); // Pass the filename to parent component if needed
    } catch (error) {
      console.error('Error uploading file:', error);
    }

    setUploading(false);
  };

  return (
    <div>
      <input type="file" accept="video/*" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={uploading}>
        {uploading ? 'Uploading...' : 'Upload Video'}
      </button>
      {videoURL && (
        <div className="video-container">
          <h2>Uploaded Video:</h2>
          <video width="600" controls>
            <source src={videoURL} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}
    </div>
  );
};

export default VideoUpload;
