import React, { useState } from 'react';

const tagsList = ['quirky', 'summer', 'hoodie'];

const AddClothForm = ({ onClose, onSave }) => {
  const [name, setName] = useState('');
  const [color, setColor] = useState('');
  const [age, setAge] = useState('');
  const [brand, setBrand] = useState('');
  const [image, setImage] = useState(null);
  const [selectedTags, setSelectedTags] = useState('');

  const tags = selectedTags.split(',').map(tag => tag.trim()).filter(tag => tag);

  const handleSubmit = async (event) => {
    event.preventDefault();

    try {
      const params = {};
      params['name'] = name;
      params['color'] = color;
      params['image'] = image;
      if (age) params['age'] = age;
      if (brand) params['brand'] = brand;
      if (tags.length > 0) {
        params['tags'] = tags;
      }

      let endpoint = `http://127.0.0.1:${process.env.REACT_APP_BACKEND_PORT}/add_dress`
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: { 'content-type': 'application/json' , 'Accept': 'application/json' },
        body: JSON.stringify(params)
      });

      if (!response.ok) {
        throw new Error('Failed to add cloth');
      }

      // Call the onSave function to refresh the catalog
      onSave();
      // Close the form
      onClose();
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      getBase64(file)
        .then((base64Image) => {
          setImage(base64Image);
        })
        .catch((error) => {
          console.error('Error converting image to base64:', error);
        });
    }
  };

  const getBase64 = (file) => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result.split(',')[1]);
      reader.onerror = (error) => reject(error);
    });
  };

  const handleTagChange = (event) => {
    const tag = event.target.value;
    setSelectedTags((prevTags) =>
      prevTags.includes(tag)
        ? prevTags.filter((t) => t !== tag)
        : [...prevTags, tag]
    );
  };

  return (
    <div className="add-cloth-form-overlay">
      <div className="add-cloth-form">
        <h2>Add New Cloth</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Name:
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
          </label>
          <label>
            Color:
            <input type="text" value={color} onChange={(e) => setColor(e.target.value)} required />
          </label>
          <label>
            Year Purchased:
            <input type="number" value={age} onChange={(e) => setAge(e.target.value)} />
          </label>
          <label>
            Brand:
            <input type="text" value={brand} onChange={(e) => setBrand(e.target.value)} />
          </label>
          <label>
            Image:
            <input type="file" accept="image/*" onChange={handleImageChange} required />
          </label>
          <label>
            Tags:
            <input type="text" value={selectedTags} onChange={(e) => setSelectedTags(e.target.value)} />
          </label>
          <button type="submit">Add Cloth</button>
          <button type="button" onClick={onClose}>Cancel</button>
        </form>
      </div>
    </div>
  );
};

export default AddClothForm;
