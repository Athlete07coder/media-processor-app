import React, { useState } from "react";
import { processMedia } from "./api";

function App() {
  const [url, setUrl] = useState("");
  const [operation, setOperation] = useState("thumbnail");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    try {
      const res = await processMedia({ url, operation });
      setResult(res.data.output);
    } catch (err) {
      alert("Error: " + err.response?.data?.detail);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Media Processor</h2>

      <input
        placeholder="Enter media URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <select onChange={(e) => setOperation(e.target.value)}>
        <option value="thumbnail">Thumbnail</option>
        <option value="compress">Compress</option>
        <option value="extract_audio">Extract Audio</option>
      </select>

      <button onClick={handleSubmit}>
        {loading ? "Processing..." : "Submit"}
      </button>

      {result && (
        <div>
          <h3>Output</h3>

          {operation === "thumbnail" && (
            <img src={`http://localhost:8000/${result}`} width="300" />
          )}

          {operation === "compress" && (
            <video controls src={`http://localhost:8000/${result}`} />
          )}

          {operation === "extract_audio" && (
            <audio controls src={`http://localhost:8000/${result}`} />
          )}
        </div>
      )}
    </div>
  );
}

export default App;