// frontend/src/App.js
import React from 'react';
import './App.css'; // Assuming you'll add some styling later
import SearchBar from './components/SearchBar';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>News Search Engine</h1>
      </header>
      <main>
        <SearchBar />
      </main>
    </div>
  );
}

export default App;