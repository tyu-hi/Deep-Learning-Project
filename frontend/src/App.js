import React, { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  // API GATEWAY ENDPOINT MISSING AT THE MOMENT!!
  const sendMessage = async () => {
    const res = await fetch("https://<API_GATEWAY_ENDPOINT>", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <h1>Chatbot</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
      <p>Chatbot Response: {response}</p>
    </div>
  );
}

export default App;
