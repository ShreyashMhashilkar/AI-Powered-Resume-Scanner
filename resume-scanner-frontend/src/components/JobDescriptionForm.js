import React from "react";
import { TextField, Box, Paper, Typography } from "@mui/material";
import WorkIcon from "@mui/icons-material/Work";

const JobDescriptionForm = ({ jd, setJd }) => (
  <Box my={4}>
    <Paper
      elevation={8}
      sx={{
        p: 4,
        borderRadius: 4,
        background: "linear-gradient(145deg, #f9f9ff, #f0f0fa)",
        boxShadow:
          "0 10px 25px rgba(42, 45, 156, 0.15), 0 6px 20px rgba(106, 13, 173, 0.1)",
      }}
    >
      {/* Heading */}
      <Typography
        variant="h5"
        gutterBottom
        sx={{
          display: "flex",
          alignItems: "center",
          gap: 1.5,
          fontWeight: "bold",
          mb: 3,
          background: "linear-gradient(90deg, #2a2d9c, #6a0dad)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
          fontSize: { xs: "1.25rem", sm: "1.5rem" },
        }}
      >
        <WorkIcon
          sx={{
            color: "#6a0dad",
            fontSize: { xs: 26, sm: 30 },
            textShadow: "0 1px 4px rgba(106,13,173,0.3)",
          }}
        />
        Job Description
      </Typography>

      {/* TextField */}
      <TextField
        multiline
        rows={6}
        fullWidth
        variant="outlined"
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        placeholder="Paste job description here..."
        sx={{
          background: "linear-gradient(180deg, #ffffff, #f7f6ff)",
          borderRadius: 3,
          "& .MuiOutlinedInput-root": {
            borderRadius: 3,
            boxShadow: "inset 0 2px 6px rgba(42, 45, 156, 0.05)",
            "& fieldset": {
              borderColor: "#dcdcf8",
            },
            "&:hover fieldset": {
              borderColor: "#6a0dad",
            },
            "&.Mui-focused fieldset": {
              borderColor: "#2a2d9c",
              boxShadow: "0 0 0 2px rgba(42, 45, 156, 0.1)",
            },
          },
        }}
        helperText="Tip: Include key skills, responsibilities, and qualifications."
      />
    </Paper>
  </Box>
);

export default JobDescriptionForm;
