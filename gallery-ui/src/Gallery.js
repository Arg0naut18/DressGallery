import React, { useState, useEffect } from 'react';

const Gallery = () => {
  const [clothes, setClothes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchClothes = async () => {
      try {
        const response = await fetch('localhost:8000/view_dress/');
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

    fetchClothes();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="clothes-catalog">
      <h1>Clothes Catalog</h1>
      <div className="clothes-grid">
        {clothes.map((item) => (
          <div key={item.id} className="clothes-item">
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
