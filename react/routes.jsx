import Loadable from 'react-loadable';
import React from 'react';

function parseJwt(token) {
    try {
        let base64Url = token.split('.')[1];
        let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        return JSON.parse(window.atob(base64));
    }
    catch(err) {
        return false;
    }
}

function getRole(tokData){
    if(tokData)
        return tokData.role;
    else
        return false
}

const userRole = getRole( parseJwt(localStorage.getItem("token")) );
console.log("ROLE - ",userRole);

function Loading() {
    return null;
}

const Dashboard = Loadable({
    loader:() => import('./views/Dashboard'),
    loading: Loading
});

const ProductList = Loadable({
    loader:() => import('./views/ProductList'),
    loading: Loading
});

const UserList = Loadable({
    loader:() => import('./views/UserList'),
    loading: Loading
});

const Icons = Loadable({
    loader:() => import('./views/Icons'),
    loading: Loading
});

const Account = Loadable({
    loader:() => import('./views/Account'),
    loading: Loading
});

const Settings = Loadable({
    loader:() => import('./views/Settings'),
    loading: Loading
});

const SignUp = Loadable({
    loader:() => import('./views/SignUp'),
    loading: Loading
});

const SignIn = Loadable({
    loader:() => import('./views/SignIn'),
    loading: Loading
});

const UnderDevelopment = Loadable({
    loader:() => import('./views/UnderDevelopment'),
    loading: Loading
});

const NotFound = Loadable({
    loader:() => import('./views/NotFound'),
    loading: Loading
});

export let routes;

routes = [
    { path: '/dashboard', exact: true, name: 'Layout', component: Dashboard },
    { path: '/products', exact: true, name: 'Product List', component: ProductList },
    { path: '/users', exact: true, name: 'User List', component: UserList },
    { path: '/icons', exact: true, name: 'Icons', component: Icons },
    { path: '/account', exact: true, name: 'Account', component: Account },
    { path: '/settings', exact: true, name: 'Settings', component: Settings },
    { path: '/sign-up', exact: true, name: 'Sign Up', component: SignUp },
    { path: '/sign-in', exact: true, name: 'Sign In', component: SignIn },
    { path: '/under-development', exact: true, name: 'Under Development', component: UnderDevelopment },
    { path: '/not-found', exact: true, name: 'Not Found', component: NotFound },
];

// import React, { Component } from 'react';
// import { Switch, Route, Redirect } from 'react-router-dom';
//
// // Views
// import Dashboard from './views/Dashboard';
// import ProductList from './views/ProductList';
// import UserList from './views/UserList';
// import Icons from './views/Icons';
// import Account from './views/Account';
// import Settings from './views/Settings';
// import SignUp from './views/SignUp';
// import SignIn from './views/SignIn';
// import UnderDevelopment from './views/UnderDevelopment';
// import NotFound from './views/NotFound';
//
// export default class Routes extends Component {
//
//     render() {
//         return (
//             <Switch>
//                 <Redirect
//                   exact
//                   from="/"
//                   to="/sign-up"
//                 />
//                 <Route
//                   component={Icons}
//                   exact
//                   path="/icons"
//                 />
//                 <Route
//                   component={SignUp}
//                   exact
//                   path="/sign-up"
//                 />
//                 <Route
//                   component={SignIn}
//                   exact
//                   path="/sign-in"
//                 />
//                 <Route
//                   component={Account}
//                   exact
//                   path="/account"
//                 />
//                 <Route
//                   component={NotFound}
//                   exact
//                   path="/not-found"
//                 />
//                 <Route
//                   component={Settings}
//                   exact
//                   path="/settings"
//                 />
//
//                 <Route
//                   component={Dashboard}
//                   exact
//                   path="/dashboard"
//                 />
//                 <Route
//                   component={UserList}
//                   exact
//                   path="/users"
//                 />
//                 <Route
//                   component={ProductList}
//                   exact
//                   path="/products"
//                 />
//                 <Route
//                   component={UnderDevelopment}
//                   exact
//                   path="/under-development"
//                 />
//                 <Redirect to="/sign-in" />
//             </Switch>
//         );
//     }
// }
