import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#283593", // deep navy blue
      light: "#5c6bc0", // calm indigo
      dark: "#1a237e", // darker shade for depth
      contrastText: "#ffffff",
    },
    secondary: {
      main: "#7e57c2", // soft purple accent
      light: "#b39ddb",
      dark: "#4a148c",
      contrastText: "#ffffff",
    },
    background: {
      default: "#f5f6fa", // subtle grey-blue background
      paper: "#ffffff", // clean white for cards
    },
    text: {
      primary: "#1a1a2e", // rich navy-black
      secondary: "#5c6b82", // soft blue-grey for subtext
    },
    success: {
      main: "#2e7d32", // muted green
    },
    error: {
      main: "#d32f2f", // calm red
    },
    warning: {
      main: "#ed6c02",
    },
    info: {
      main: "#3949ab",
    },
  },

  typography: {
    fontFamily: `'Inter', 'Poppins', 'Roboto', sans-serif`,
    h4: {
      fontWeight: 700,
      color: "#1a237e",
      letterSpacing: "0.01em",
    },
    h6: {
      fontWeight: 600,
      color: "#283593",
    },
    body1: {
      color: "#1a1a2e",
      lineHeight: 1.6,
    },
    body2: {
      color: "#5c6b82",
    },
    button: {
      textTransform: "none",
      fontWeight: 600,
      letterSpacing: "0.02em",
    },
  },

  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          fontWeight: 600,
          padding: "10px 20px",
          backgroundColor: "#283593",
          color: "#fff",
          transition: "all 0.3s ease",
          "&:hover": {
            backgroundColor: "#1a237e",
            boxShadow: "0 4px 12px rgba(40,53,147,0.3)",
          },
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow:
            "0px 3px 8px rgba(0,0,0,0.05), 0px 1px 4px rgba(0,0,0,0.08)",
          transition: "all 0.3s ease",
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          background:
            "linear-gradient(180deg, #ffffff 0%, #f3f4fa 100%)",
          boxShadow:
            "0px 3px 10px rgba(0,0,0,0.05), 0px 1px 3px rgba(0,0,0,0.1)",
          transition: "all 0.3s ease",
          "&:hover": {
            transform: "translateY(-3px)",
            boxShadow:
              "0px 6px 16px rgba(40,53,147,0.15), 0px 3px 8px rgba(126,87,194,0.1)",
          },
        },
      },
    },
  },
});

export default theme;
