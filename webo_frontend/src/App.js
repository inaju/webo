import logo from "./logo.svg";
import "./App.css";
import General from "./Pages/General/General";
import Analysis from "./Pages/Analysis/Analysis";
import Visualization from "./Pages/Visualization/Visualization";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={General} exact />
        <Route exact path="/analysis" component={Analysis} />
        <Route exact path="/visualization" component={Visualization} />
      </Switch>
    </Router>
  );
}

export default App;
