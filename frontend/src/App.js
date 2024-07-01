import logo from "./logo.svg";
import "./App.css";
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [data, SetData] = useState({
    name: "",
    email: "",
    text: "",
  });

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("title", data.title);
    formData.append("email", data.email);
    formData.append("message", data.text);

    await axios.post("http://127.0.0.1:8000/app/data/", formData)
      .then((res) => {
        console.log(res);
        SetData((prevData) => ({
          ...prevData,
          title: "",
          email: "",
          text: "",
        }));
      })
      .catch((error) => {
        console.log(error);
      });
    
  };
  // useEffect(()=>{
  // },[data])

  const inputHandler = (e) => {
    SetData({
      ...data,
      [e.target.name]: e.target.value,
    });
  };

  //  console.log(data)

  return (
    <div>
      <input
        placeholder="Title"
        className="input"
        name="title"
        type="text"
        value={data.title}
        onChange={inputHandler}
      />
      <br />
      <br />
      <input
        placeholder="Email address"
        className="input"
        name="email"
        type="email"
        value={data.email}
        onChange={inputHandler}
      />
      <br />
      <br />
      <textarea
        placeholder="Message"
        className="input"
        name="text"
        value={data.text}
        onChange={inputHandler}
      ></textarea>
      <br />
      <br />
      <button className="button type1">
        <span className="btn-txt" onClick={handleSubmit}>
          Submit
        </span>
      </button>
    </div>
  );
}

export default App;
