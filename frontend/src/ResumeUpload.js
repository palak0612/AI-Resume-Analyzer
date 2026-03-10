import React, { useState } from "react";
import axios from "axios";

function ResumeUpload() {
  const [file, setFile] = useState(null);
  const [skills, setSkills] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("resume", file);
    formData.append("skills", skills);

    const response = await axios.post(
      "http://127.0.0.1:5000/analyze",
      formData
    );

    setResult(response.data);
  };

  return (
    <div>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />

      <br /><br />

      <input
        type="text"
        placeholder="Enter skills (python,java,react)"
        onChange={(e) => setSkills(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>Analyze Resume</button>

      {result && (
        <div>
          <h3>Score: {result.score}%</h3>
          <p>Matched Skills: {result.matched_skills.join(", ")}</p>
        </div>
      )}
    </div>
  );
}

export default ResumeUpload;