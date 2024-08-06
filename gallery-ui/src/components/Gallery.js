import React, { useEffect, useState } from 'react';

const Gallery = () => {
  const [clothes, setClothes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [searchTerm, setSearchTerm] = useState('');
  const [selectedTags, setSelectedTags] = useState([]);
  const [ageFilter, setAgeFilter] = useState('');
  const [colorFilter, setColorFilter] = useState('');

  const [filters, setFilters] = useState({
    searchTerm: '',
    selectedTags: [],
    ageFilter: '',
    colorFilter: ''
  });

  useEffect(() => {
    const fetchClothes = async () => {
      setLoading(true);
      setError(null);
      try {
        const params = new URLSearchParams();
        if (searchTerm) params.append('name', searchTerm);
        if (ageFilter) params.append('max_age', ageFilter);
        if (colorFilter) params.append('color', colorFilter);
        if (selectedTags.length > 0) params.append('tags', selectedTags.join(','));
        const response = await fetch(`http://127.0.0.1:8000/view_dress?${params.toString()}`);
        if (!response.ok) {
          throw new Error('Failed to fetch clothes');
        }
        const data = await response.json();
        setClothes(data.Message);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

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
    const tag = event.target.value;
    setSelectedTags((prevTags) =>
      prevTags.includes(tag)
        ? prevTags.filter((t) => t !== tag)
        : [...prevTags, tag]
    );
  };

  const handleAgeChange = (event) => {
    setAgeFilter(event.target.value);
  };

  const handleColorChange = (event) => {
    setColorFilter(event.target.value);
  };

  const applyFilters = () => {
    setFilters({
      searchTerm,
      selectedTags,
      ageFilter,
      colorFilter
    });
  };

  const resetFilters = () => {
    setSearchTerm('');
    setSelectedTags([]);
    setAgeFilter('');
    setColorFilter('');
    setFilters({
      searchTerm: '',
      selectedTags: [],
      ageFilter: '',
      colorFilter: ''
    });
  };

  return (
    <div className="clothes-catalog">
      <h1 className='title'>Clothes Catalogue</h1>
      <div className="filters">
        <input
          type="text"
          placeholder="Search by name"
          className='name-search'
          value={searchTerm}
          onChange={handleSearchChange}
        />
        <input
          type="number"
          placeholder="Age (in months)"
          className='age-search'
          value={ageFilter}
          onChange={handleAgeChange}
        />
        <input
          type="text"
          placeholder="Color"
          className='color-search'
          value={colorFilter}
          onChange={handleColorChange}
        />
        <div className="tags">
          <label>
            <input type="checkbox" value="quirky" className="checkbox" onChange={handleTagChange} />
            Quirky
          </label>
          <label>
            <input type="checkbox" value="summer" className="checkbox" onChange={handleTagChange} />
            Summer
          </label>
        </div>
        <button onClick={applyFilters}>Apply Filters</button>
        <button onClick={resetFilters}>Reset Filters</button>
      </div>
      <div className="clothes-grid">
        {clothes.map((item) => (
          <div key={item.name} className="clothes-item">
            <img src={`data:image/jpeg;base64,${item.image}`} alt={item.name} />
            <h2>{item.name}</h2>
            <p>{item.color}</p>
            {item.brand && <p>{item.brand}</p>}
            {item.tags && <p>{item.tags}</p>}
            {item.age && <p>{item.age}</p>}
            {item.purchased_date && <p>{item.purchased_date}</p>}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Gallery;
