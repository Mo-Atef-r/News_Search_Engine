// frontend/src/components/SearchBar.js
import React, { useState } from 'react';

const SearchBar = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/search/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query }),
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error fetching search results:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for articles..."
        />
        <button type="submit">Search</button>
      </form>
  
      {results.length > 0 && (
        <ul className="results-list">
          {results.map((result) => (
            <li key={result.id} className="result-item">
              <h3 className="result-score">Score: {result.score.toFixed(4)}</h3>
              <p className="result-content">{result.content}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchBar;