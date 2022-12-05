import React,{useState} from 'react'
import MapImage from '../src/assets/map.png';
import { mapLevels, allCitiesMap } from './citiesMock';
import './App.css';

function App() {
  const [userLevel, setUserLevel] = useState('')
  const [cities, setCities] = useState([])
  const [route, setRoute] = useState([])
  const [userCity, setUserCity] = useState('')
  const [destinyCity, setDestinyCity] = useState('')
  const [showCities, setShowCities] = useState(false)
  const [loadingResult, setLoadingResult] = useState(false)

  function handleChangeUserLevel(value){
    setUserLevel(value)
  }

  function handleSubmitLevel(){

    let response = mapLevels.filter(city => Number(userLevel) >= city.minLevel)
    
    console.log("handleSubmitLevel", response)
    setCities(response)
    setShowCities(true)
  }

  function handleChangeCity(value){
    setUserCity(value)
  }

  function handleChangeDestinyCity(value){
    setDestinyCity(value)
  }

  function handleSubmitCity(){
    fetch(`http://localhost:8000/graph?city_i=${userCity}&city_d=${destinyCity}`)
    .then((response) => response.json())
    .then((data) => {
      setLoadingResult(true)
      setRoute(data)
      console.log(data)
    });
    
  }

  function handleResetForm(){
    setUserCity('')
    setDestinyCity('')
    setUserLevel('')
    setShowCities(false)
    setLoadingResult(false)
  }

  return (
    <div className="App">
      <div className='content'>
        <div className='map'>
          <img src={MapImage} className="odyssey-map" alt="map" />
        </div>
        <div className='form'>
          <h1 className='title'>
            Odyssey Level Route
          </h1>
          <div id="step-level" className='widget-question'>
            <h3>Insira seu nível (1-19):</h3>
            
            <div className='input-container'>
              <input onChange={(e)=> handleChangeUserLevel(e.target.value)}
                type="number" 
                min="1" 
                max="19" 
                value={userLevel} 
                name="level" 
                className="input"/>

              <button onClick={handleSubmitLevel} className="button">Enviar</button>
            </div>
          </div>

          {showCities && (
            <div id="step-city" className='widget-question'>
              <h3>Selecione as cidades:</h3>           
              <div className='input-container'>
                <select value={userCity} name="cities" id="cities" onChange={(e)=> handleChangeCity(e.target.value)}>
                  <option>Selecione uma cidade de início</option>
                  {cities?.map(city => 
                    <option key={city.name} value={city.name}>
                      {city.name}
                    </option>
                  )}
                </select>
                <select value={destinyCity} name="allCities" id="allCities" onChange={(e)=> handleChangeDestinyCity(e.target.value)}>
                  <option>Selecione uma cidade de destino</option>
                  {allCitiesMap?.map(city => 
                    <option key={city} value={city}>
                      {city}
                    </option>
                  )}
                </select>
                <button onClick={handleSubmitCity} className="button">Enviar</button>
              </div>
            </div>
          )}

          {loadingResult && (
            <div id="step-route" className='widget-question'>
              <h3>A melhor rota para {destinyCity} considerando a distância e o nível das cidades é:</h3>
              <p>{route[0]}</p>
              <h3>Com a distância de:<span className="min-dist"> {route[1]}</span></h3>
              <button onClick={handleResetForm}>Refazer</button>
            </div>
          )}

        </div>
      </div>
    </div>
  )
}

export default App;
