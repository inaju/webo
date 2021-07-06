import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import General from './Pages/General/General';
import Analysis from './Pages/Analysis/Analysis';
import Visualization from './Pages/Visualization/Visualization';

function App() {
  return (
    <div className="App">
      
      <Switch>
      <div className="app-component">
                <Route path="/" component={General} exact />
                <Route path="/analysis" component={Analysis} />
                <Route path="/visualization" component={Visualization} />
            
      </div>
      </Switch>
    </div>
  );
}

export default App;
