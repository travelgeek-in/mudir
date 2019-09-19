export default theme => ({
    root: {
        backgroundColor: theme.palette.background.default,
        height: '100vh'
    },
    grid: {
        height: '100%'
    },
    quoteWrapper: {
        [theme.breakpoints.down('md')]: {
            display: 'none'
        }
    },
    quote: {
        backgroundColor: theme.palette.custom.dark,
        height: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center'
    },
    quoteInner: {
        textAlign: 'center',
        flexBasis: '600px'
    },
    quoteText: {
        color: theme.palette.common.white,
        fontWeight: 600,
        fontSize:25,

    },
    name: {
        marginTop: theme.spacing(3),
        color: theme.palette.common.white
    },
    bio: {
        color: theme.palette.common.white
    },
    contentWrapper: {},
    content: {
        height: '100%',
        display: 'flex',
        flexDirection: 'column'
    },
    contentHeader: {
        display: 'flex',
        alignItems: 'center',
        paddingTop: theme.spacing(5),
        paddingBototm: theme.spacing(2),
        paddingLeft: theme.spacing(2),
        paddingRight: theme.spacing(2)
    },
    backButton: {},
    logoImage: {
        marginLeft: theme.spacing(4)
    },
    contentBody: {
        flexGrow: 1,
        display: 'flex',
        alignItems: 'center',
        [theme.breakpoints.down('md')]: {
            justifyContent: 'center'
        },
        margin: '0px 70px',
        [theme.breakpoints.down('md')]: {
            margin: '0px'
        }
    },
    form: {
        paddingLeft: '100px',
        paddingRight: '100px',
        paddingBottom: '50px',
        flexBasis: '700px',
        [theme.breakpoints.down('sm')]: {
            paddingLeft: theme.spacing(2),
            paddingRight: theme.spacing(2)
        }
    },
    title: {
        marginTop: theme.spacing(3)
    },
    subtitle: {
        color: theme.palette.text.secondary,
        marginTop: theme.spacing(0.5)
    },
    facebookButton: {
        marginTop: theme.spacing(3),
        width: '100%'
    },
    facebookIcon: {
        marginRight: theme.spacing()
    },
    googleButton: {
        marginTop: theme.spacing(2),
        width: '100%'
    },
    googleIcon: {
        marginRight: theme.spacing()
    },
    sugestion: {
        color: theme.palette.text.secondary,
        marginTop: theme.spacing(2),
        textAlign: 'center'
    },
    fields: {
        marginTop: theme.spacing(2)
    },
    textField: {
        width: '100%',
        '& + & ': {
            marginTop: theme.spacing(2)
        }
    },
    policy: {
        display: 'flex',
        alignItems: 'center'
    },
    policyCheckbox: {
        marginLeft: '-14px'
    },
    policyText: {
        display: 'inline',
        color: theme.palette.text.secondary
    },
    policyUrl: {
        color: theme.palette.text.primary,
        '&:hover': {
            cursor: 'pointer',
            color: theme.palette.primary.main
        }
    },
    progress: {
        display: 'block',
        marginTop: theme.spacing(2),
        marginLeft: 'auto',
        marginRight: 'auto'
    },
    signInButton: {
        marginTop: theme.spacing(2),
        width: '100%'
    },
    signUp: {
        marginTop: theme.spacing(4),
        color: theme.palette.text.secondary
    },
    signUpUrl: {
        color: theme.palette.primary.main,
        fontWeight: 'bold',
        '&:hover': {
            color: theme.palette.primary.main
        },
        textDecoration:'none'
    },
    fieldError: {
        color: theme.palette.danger.main,
        marginBottom: theme.spacing(2),
        marginTop: theme.spacing.unit
    },
    submitError: {
        color: theme.palette.danger.main,
        alignText: 'center',
        marginBottom: theme.spacing(),
        marginTop: theme.spacing(2)
    },
    loginImage: {
        width: '50%',
        transform: 'translate(0%, 30%)'
    }
});
