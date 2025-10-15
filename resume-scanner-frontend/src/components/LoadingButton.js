import React from "react";
import { Button, CircularProgress, Box } from "@mui/material";
import RocketLaunchIcon from "@mui/icons-material/RocketLaunch";

const LoadingButton = ({ onClick, loading }) => (
  <Box my={3}>
    <Button
      variant="contained"
      color="primary"
      onClick={onClick}
      disabled={loading}
      fullWidth
      size="large"
      startIcon={!loading ? <RocketLaunchIcon /> : null}
      sx={{ fontWeight: "bold", fontSize: 16 }}
    >
      {loading ? <CircularProgress size={24} /> : "Match & Rank Resumes"}
    </Button>
  </Box>
);

export default LoadingButton;
