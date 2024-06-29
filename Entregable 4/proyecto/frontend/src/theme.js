// src/theme.js

import { createTheme } from '@material-ui/core/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#3f51b5',
    },
    secondary: {
      main: '#f50057',
    },
  },
  typography: {
    fontFamily: 'Roboto, sans-serif',
    fontSize: 10, // Tamaño de la fuente ajustado a 10
  },
});

export default theme;
