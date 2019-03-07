import React from 'react';
import withStyles from '@material-ui/styles/withStyles';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';

import CommonParametersMeta from './Params/CommonMeta';
import CommonParametersSpec from './Params/CommonSpec';
import SuggestionSpec from './Params/SuggestionSpec';
import WorkerSpecParam from './Params/Worker';


import { connect } from 'react-redux';
import NASConfig from './Params/NASConfig';

const module = "nasCreate";

const styles = theme => ({
    root: {
        width: '90%',
        margin: '0 auto',
    },
    submit: {
        textAlign: 'center',
        marginTop: 10,
    },
    textField: {
        marginLeft: 4,
        marginRight: 4,
        width: '100%'
    },
    help: {
        padding: 4 / 2,
        verticalAlign: "middle",
    },
    section: {
        padding: 4,
    },
    parameter: {
        padding: 2,
    },
    formControl: {
        margin: 4,
        width: '100%',
    },
    selectEmpty: {
        marginTop: 10,
    },
    addButton: {
        margin: 10,
    }
})

const SectionInTypography = (name, classes) => {
    return (
        <div className={classes.section}>
            <Grid container>
                <Grid item xs={12} sm={12}>
                    <Typography variant="h6">
                        {name}
                    </Typography>
                <hr />
                </Grid>
            </Grid>
        </div>
    )
}

// probably get render into a function

const NASParameters = (props) => {
    const { classes } = props;
    return (
            <div className={classes.root}>
                {/* Common Metadata */}
                {SectionInTypography("Metadata", classes)}
                <CommonParametersMeta />
                {SectionInTypography("Spec", classes)}
                <CommonParametersSpec />
                {SectionInTypography("NAS Config", classes)}
                <NASConfig />
                {SectionInTypography("Worker Spec", classes)}
                <WorkerSpecParam />
                {SectionInTypography("Suggestion Parameters", classes)} 
                <SuggestionSpec />
                <div className={classes.submit}>
                    <Button variant="contained" color={"primary"} className={classes.button}>
                        Deploy
                    </Button>
                </div>                
            </div>
    )
}

export default connect(null, null)(withStyles(styles)(NASParameters));