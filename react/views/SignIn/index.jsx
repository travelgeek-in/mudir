import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';

// Externals
import PropTypes from 'prop-types';
import compose from 'recompose/compose';
import validate from 'validate.js';
import _ from 'underscore';

import { withStyles } from '@material-ui/core';

import {
    Grid,
    Button,
    IconButton,
    CircularProgress,
    TextField,
    Typography
} from '@material-ui/core';

import { ArrowBack as ArrowBackIcon } from '@material-ui/icons';

import { Facebook as FacebookIcon, Google as GoogleIcon } from '../../icons';

import styles from './styles';

import schema from './schema';
import apiHandler from "../../apiHandler";
import axios from 'axios';
let tokenHeader = {
    headers: {'Authorization': "jwt " + localStorage.getItem('token')}
};

class SignIn extends Component {
    state = {
        values: {
            email: '',
            password: ''
        },
        touched: {
            email: false,
            password: false
        },
        errors: {
            email: null,
            password: null
        },
        isValid: false,
        isLoading: false,
        submitError: null
    };


    componentDidMount() {
        console.log(tokenHeader);
    }

    handleBack = () => {
        const { history } = this.props;

        history.goBack();
    };

    validateForm = _.debounce(() => {
        const { values } = this.state;

        const newState = { ...this.state };
        const errors = validate(values, schema);

        newState.errors = errors || {};
        newState.isValid = !errors;

        this.setState(newState);
    }, 300);

    handleFieldChange = (field, value) => {
        const newState = { ...this.state };

        newState.submitError = null;
        newState.touched[field] = true;
        newState.values[field] = value;

        this.setState(newState, this.validateForm);
    };

    handleSignIn = () => {
        let this_ = this;
        const { history } = this.props;
        const { values } = this.state;

        this.setState({ isLoading: true });
        let data = {};
        data['username_or_email'] = values.email;
        data['password'] = values.password;
        axios.post(apiHandler.login, data).then(res => {
            localStorage.setItem('isAuthenticated', true);
            localStorage.setItem('token', res.data.token);
            history.push('/dashboard');
        }).catch(function (error) {
            this_.setState({
                isLoading: false,
                serviceError: error.response.data.non_field_errors[0]
            });
        });
    };

    render() {
        const { classes } = this.props;
        const {
            values,
            touched,
            errors,
            isValid,
            submitError,
            isLoading
        } = this.state;

        const showEmailError = touched.email && errors.email;
        const showPasswordError = touched.password && errors.password;

        return (
            <div className={classes.root}>
                <Grid
                    className={classes.grid}
                    container
                >
                    <Grid
                        className={classes.quoteWrapper}
                        item
                        lg={4}
                    >
                        <div className={classes.quote}>
                            <div className={classes.quoteInner}>
                                <Typography
                                    className={classes.quoteText}
                                    variant="h1"
                                >
                                    Software For Travel companies Firms That Want To Grow Faster.
                                </Typography>
                                <div className={classes.imageWrapper}>
                                    <img
                                        alt="Product"
                                        className={classes.loginImage}
                                        src={'/static/images/login-page-left-image-new.svg'}
                                    />
                                </div>
                                {/*<div className={classes.person}>*/}
                                {/*    <Typography*/}
                                {/*        className={classes.name}*/}
                                {/*        variant="body1"*/}
                                {/*    >*/}
                                {/*        Takamaru Ayako*/}
                                {/*    </Typography>*/}
                                {/*    <Typography*/}
                                {/*        className={classes.bio}*/}
                                {/*        variant="body2"*/}
                                {/*    >*/}
                                {/*        Manager at inVision*/}
                                {/*    </Typography>*/}
                                {/*</div>*/}
                            </div>
                        </div>
                    </Grid>
                    <Grid
                        className={classes.content}
                        item
                        lg={8}
                        xs={12}
                    >
                        <div className={classes.content}>
                            <div className={classes.contentHeader}>
                                <IconButton
                                    className={classes.backButton}
                                    onClick={this.handleBack}
                                >
                                    <ArrowBackIcon />
                                </IconButton>
                            </div>
                            <div className={classes.contentBody}>
                                <form className={classes.form}>
                                    <Typography
                                        className={classes.title}
                                        variant="h2"
                                    >
                                        Sign in
                                    </Typography>
                                    {/*<Typography*/}
                                    {/*    className={classes.subtitle}*/}
                                    {/*    variant="body1"*/}
                                    {/*>*/}
                                    {/*    Sign in with social media*/}
                                    {/*</Typography>*/}
                                    {/*<Button*/}
                                    {/*    className={classes.facebookButton}*/}
                                    {/*    color="primary"*/}
                                    {/*    onClick={this.handleSignIn}*/}
                                    {/*    size="large"*/}
                                    {/*    variant="contained"*/}
                                    {/*>*/}
                                    {/*    <FacebookIcon className={classes.facebookIcon} />*/}
                                    {/*    Login with Facebook*/}
                                    {/*</Button>*/}
                                    {/*<Button*/}
                                    {/*    className={classes.googleButton}*/}
                                    {/*    onClick={this.handleSignIn}*/}
                                    {/*    size="large"*/}
                                    {/*    variant="contained"*/}
                                    {/*>*/}
                                    {/*    <GoogleIcon className={classes.googleIcon} />*/}
                                    {/*    Login with Google*/}
                                    {/*</Button>*/}
                                    {/*<Typography*/}
                                    {/*    className={classes.sugestion}*/}
                                    {/*    variant="body1"*/}
                                    {/*>*/}
                                    {/*    or login with email address*/}
                                    {/*</Typography>*/}
                                    <div className={classes.fields}>
                                        <TextField
                                            className={classes.textField}
                                            label="Email address or Username"
                                            name="email"
                                            onChange={event =>
                                                this.handleFieldChange('email', event.target.value)
                                            }
                                            type="text"
                                            value={values.email}
                                            variant="outlined"
                                        />
                                        {showEmailError && (
                                            <Typography
                                                className={classes.fieldError}
                                                variant="body2"
                                            >
                                                {errors.email[0]}
                                            </Typography>
                                        )}
                                        <TextField
                                            className={classes.textField}
                                            label="Password"
                                            name="password"
                                            onChange={event =>
                                                this.handleFieldChange('password', event.target.value)
                                            }
                                            type="password"
                                            value={values.password}
                                            variant="outlined"
                                        />
                                        {showPasswordError && (
                                            <Typography
                                                className={classes.fieldError}
                                                variant="body2"
                                            >
                                                {errors.password[0]}
                                            </Typography>
                                        )}
                                    </div>
                                    <Grid className={classes.grid} container>
                                        <Grid lg={8} xs={6}>
                                            <Typography className={classes.signUp} variant="body1">
                                                Don't have an account?{' '}
                                                <Link
                                                    className={classes.signUpUrl}
                                                    to="/sign-up"
                                                >
                                                    Sign up
                                                </Link>
                                            </Typography>
                                        </Grid>
                                        <Grid lg={4} xs={6}>
                                            {submitError && (
                                                <Typography className={classes.submitError} variant="body2">
                                                    {submitError}
                                                </Typography>
                                            )}
                                            {isLoading ? (
                                                <CircularProgress className={classes.progress} />
                                            ) : (
                                                <Button
                                                    className={classes.signInButton}
                                                    color="primary"
                                                    disabled={!isValid}
                                                    onClick={this.handleSignIn}
                                                    size="large"
                                                    variant="contained"
                                                >
                                                    Sign in now
                                                </Button>
                                            )}
                                        </Grid>
                                    </Grid>
                                </form>
                            </div>
                        </div>
                    </Grid>
                </Grid>
            </div>
        );
    }
}

SignIn.propTypes = {
    className: PropTypes.string,
    classes: PropTypes.object.isRequired,
    history: PropTypes.object.isRequired
};

export default compose(
    withRouter,
    withStyles(styles)
)(SignIn);
