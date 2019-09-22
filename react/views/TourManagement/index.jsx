import React, { Component } from 'react';
import { Link, withRouter } from 'react-router-dom';

import styles from './styles';
import apiHandler from "../../apiHandler";
import axios from 'axios';
import PropTypes from "prop-types";
import compose from "recompose/compose";
import {IconButton, Typography, withStyles} from "@material-ui/core";
import {Dashboard as DashboardLayout} from "../../layouts";
import VerticalLinearStepper from "../../Steppers";

let tokenHeader = {
    headers: {'Authorization': "jwt " + localStorage.getItem('token')}
};

class Tour extends React.Component{
    state = {};

    handleBack = () => {
        const { history } = this.props;
        history.goBack();
    };

    render() {

        const { classes } = this.props;
        return(
            <DashboardLayout title="Tour Management">
                <div className={classes.root}>
                    <div className={classes.content}>
                        <Typography
                            className={classes.nameText}
                            variant="h6"
                        >
                            Tour Management
                        </Typography>
                    </div>
                </div>

                <VerticalLinearStepper/>
            </DashboardLayout>
        )
    }
}

Tour.propTypes = {
    className: PropTypes.string,
    classes: PropTypes.object.isRequired,
    history: PropTypes.object.isRequired
};

export default compose(
    withRouter,
    withStyles(styles)
)(Tour);
