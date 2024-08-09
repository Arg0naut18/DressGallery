import React, { useEffect, useState } from 'react';
import DressForm from './DressForm';

const Gallery = () => {
  const [clothes, setClothes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTags, setSelectedTags] = useState('');
  const [ageFilter, setAgeFilter] = useState('');
  const [colorFilter, setColorFilter] = useState('');
  const [brandFilter, setBrandFilter] = useState('');

  const [filters, setFilters] = useState({
    searchTerm: '',
    selectedTags: [],
    ageFilter: '',
    colorFilter: ''
  });

  const [showForm, setShowForm] = useState(false);

  const fetchClothes = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams();
      params.append('name', filters.searchTerm);
      params.append('color', filters.colorFilter);
      if (filters.ageFilter) params.append('max_age', filters.ageFilter);
      if (filters.brandFilter) params.append('brand', filters.brandFilter);
      if (filters.selectedTags) params.append('tags', filters.selectedTags);

      let finalUrl = `http://127.0.0.1:${process.env.REACT_APP_BACKEND_PORT}/view_dress?${params.toString()}`;

      const response = await fetch(finalUrl);
      if (!response.ok) {
        throw new Error('Failed to fetch clothes');
      }
      const data = await response.json();
      setClothes(data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchClothes();
  }, [filters]);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  const handleSearchChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleTagChange = (event) => {
    setSelectedTags(event.target.value);
  };

  const handleAgeChange = (event) => {
    setAgeFilter(event.target.value);
  };

  const handleColorChange = (event) => {
    setColorFilter(event.target.value);
  };

  const handleBrandChange = (event) => {
    setBrandFilter(event.target.value);
  };

  const applyFilters = () => {
    setFilters({
      searchTerm,
      selectedTags,
      ageFilter,
      colorFilter,
      brandFilter
    });
  };

  const resetFilters = () => {
    setSearchTerm('');
    setSelectedTags('');
    setAgeFilter('');
    setColorFilter('');
    setBrandFilter('');
    setFilters({
      searchTerm: '',
      selectedTags: '',
      ageFilter: '',
      colorFilter: '',
      brandFilter: ''
    });
  };

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  return (
    <div className="clothes-catalog">
      <h1 className='title'>Clothes Catalogue</h1>
      <div className="filters">
        Name:
        <input
          type="text"
          placeholder="Search by name"
          className='name-search'
          value={searchTerm}
          onChange={handleSearchChange}
        />
        Year Purchased:
        <input
          type="number"
          placeholder="Year"
          className='age-search'
          value={ageFilter}
          onChange={handleAgeChange}
        />
        Color:
        <input
          type="text"
          placeholder="Color"
          className='color-search'
          value={colorFilter}
          onChange={handleColorChange}
        />
        Brand:
        <input
          type="text"
          placeholder="Brand"
          className='brand-search'
          value={brandFilter}
          onChange={handleBrandChange}
        />
        Tags:
        <div className="tags">
        <input
          type="text"
          placeholder="Tags separated by ,"
          className='tags-search'
          value={selectedTags}
          onChange={handleTagChange}
        />
        </div>
        <button onClick={applyFilters}>Apply Filters</button>
        <button onClick={resetFilters}>Reset Filters</button>
      </div>
      <div className="clothes-grid">
        {clothes.map((item) => (
          <div key={item.name} className="clothes-item">
            <img src={`data:image/jpeg;base64,${item.image}`} alt={item.name} />
            <h2>{item.name}</h2>
            <p>Color: {item.color}</p>
            {item.brand && <p>Brand: {item.brand}</p>}
            {item.age && <p>Age: {item.age}</p>}
            {item.purchased_date && <p>Purchased Date: {item.purchased_date}</p>}
            {item.tags?.slice(0, 5).map((tag) => (
              <p key={tag}>{tag}</p>
            ))}
          </div>
        ))}
      </div>
      <button className="floating-button" onClick={toggleForm}>+</button>
      {showForm && <DressForm onClose={toggleForm} onSave={fetchClothes} />}
    </div>
  );
};

export default Gallery;
