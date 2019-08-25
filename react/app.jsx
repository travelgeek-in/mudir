import React, { Component } from 'react';
import { Redirect, Route, Switch, HashRouter } from 'react-router-dom';

// Externals
// import { Chart } from 'react-chartjs-2';

// Material helpers
import { ThemeProvider } from '@material-ui/styles';

// ChartJS helpers
// import { chartjs } from './helpers';

// Theme
import theme from './theme';

// Styles
import 'react-perfect-scrollbar/dist/css/styles.css';
import './assets/scss/index.scss';

// Routes
import {routes} from './routes';

// Configure ChartJS
// Chart.helpers.extend(Chart.elements.Rectangle.prototype, {
//   draw: chartjs.draw
// });

export default class App extends Component {
  loading = () =>  <div className="animated fadeIn pt-1 text-center">Loading...</div>;
  render() {
    return (
        <ThemeProvider theme={theme}>
            <HashRouter>
                <Switch>
                    {
                        routes.map((route, id) => {
                            return route.component ? (
                                <Route
                                    key={id}
                                    path={route.path}
                                    exact={route.exact}
                                    name={route.name}
                                    render={props =>
                                        <route.component {...props}/>
                                    }
                                />
                            ) : (null);
                        })
                    }
                    <Redirect to="/dashboard" />
                </Switch>
            </HashRouter>
        </ThemeProvider>
    );
  }
}
