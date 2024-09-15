import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Placeholder components for now, will create later
const Login = () => <div>Login Page</div>;
const Dashboard = () => <div>Dashboard Page</div>;

const AppRouter = () => (
  <Router>
    <Switch>
      <Route path="/login" component={Login} />
      <Route path="/dashboard" component={Dashboard} />
      <Route path="/" component={Login} />
    </Switch>
  </Router>
);

export default AppRouter;
