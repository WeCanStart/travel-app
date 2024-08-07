import React from 'react';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import './App.css';

import { SightPrinter } from './SightPrinter.jsx';

export class App extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      city: "null",
      sights: {
        "geo": [],
        "msk": [],
        "spb": [],
        "nsk": [],
        "ekb": [],
        "kzn": [],
        "nn": []
      }
    };
  }

  handleChange = (event) => {
    this.setState({ city: event?.target?.value });
  }

  render() {
    return (
      <Router>
        <Routes>
          <Route path="/" element = {
            <div>
              <select name="location" value={this.state.city} onChange={this.handleChange}>
                <option default value="null">Выберите город</option>
                <option value="geo">Геолокация</option>
                <option value="msk">Москва</option>
                <option value="spb">Санкт-Петербург</option>
                <option value="nsk">Новосибирск</option>
                <option value="ekb">Екатеринбург</option>
                <option value="kzn">Казань</option>
                <option value="nn">Нижний Новгород</option>
              </select>
              <SightPrinter city={this.state.city}/>
            </div>
          }/>
            
          <Route path="/login" element = {
            <div>
              <form className="login" /*</div>onSubmit={this.handleSubmit}*/ >
                <input type="text" name="email" placeholder="email" />
                <input type="password" name="password" placeholder="password" />
                <button name="login" /*onClick={this.handleLogin}*/>Войти</button>
              </form>
              <button name="register" /*onClick={this.handleRegister}*/>Зарегистрироваться</button>
            </div>
          }/>
        </Routes>
      </Router>
    );
  }
}
