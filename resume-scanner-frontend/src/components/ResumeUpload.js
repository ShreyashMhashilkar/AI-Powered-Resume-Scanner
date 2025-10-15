import React, { useState } from "react";
import {
  Box,
  Button,
  List,
  ListItem,
  ListItemText,
  Typography,
  Paper,
  Fade,
} from "@mui/material";
import UploadFileIcon from "@mui/icons-material/UploadFile";
import DescriptionIcon from "@mui/icons-material/Description";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";

const ResumeUpload = ({ resumes, setResumes }) => {
  const [uploadSuccess, setUploadSuccess] = useState(false);

  const handleFileChange = (e) => {
    const files = Array.from(e.target.files);
    if (files.length > 0) {
      setResumes((prevResumes) => [...prevResumes, ...files]);
      setUploadSuccess(true);
      setTimeout(() => setUploadSuccess(false), 2000); // Hide message after 2 sec
    }
  };

  return (
    <Box my={3}>
      <Box display="flex" alignItems="center" justifyContent="space-between">
        {/* Upload Button (Left-aligned) */}
        <Box>
          <input
            accept=".txt,.pdf,.docx"
            id="upload-resume"
            multiple
            type="file"
            style={{ display: "none" }}
            onChange={handleFileChange}
          />
          <label htmlFor="upload-resume">
            <Button
              variant="contained"
              color="primary"
              component="span"
              startIcon={<UploadFileIcon />}
              sx={{
                background: "linear-gradient(90deg, #2a2d9c, #6a0dad)",
                boxShadow: "0px 4px 10px rgba(106, 13, 173, 0.4)",
                "&:hover": {
                  background: "linear-gradient(90deg, #1f2180, #5a0ca5)",
                  boxShadow: "0px 6px 14px rgba(106, 13, 173, 0.5)",
                },
              }}
            >
              Upload Resumes
            </Button>
          </label>
        </Box>

        {/* Success Message (Centered in horizontal space) */}
        <Fade in={uploadSuccess}>
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 1,
              mx: "auto",
              color: "#4CAF50",
              fontWeight: "bold",
            }}
          >
            <CheckCircleIcon color="success" />
            <Typography variant="subtitle1">
              File(s) uploaded successfully!
            </Typography>
          </Box>
        </Fade>
      </Box>

      {/* File list */}
      {resumes.length > 0 && (
        <Paper
          elevation={6} // Increased elevation
          sx={{
            mt: 3,
            p: 3,
            borderRadius: 3,
            backgroundColor: "#fafaff",
            boxShadow:
              "0px 4px 12px rgba(42, 45, 156, 0.2), 0px 6px 18px rgba(106, 13, 173, 0.2)",
          }}
        >
          <Typography variant="h6" gutterBottom color="primary" fontWeight="bold">
            Selected Files:
          </Typography>
          <List dense>
            {resumes.map((file, idx) => (
              <ListItem
                key={idx}
                sx={{
                  borderBottom: "1px solid #eee",
                  display: "flex",
                  alignItems: "center",
                  gap: 1,
                }}
              >
                <DescriptionIcon sx={{ color: "#6a0dad" }} />
                <ListItemText
                  primary={file.name}
                  primaryTypographyProps={{
                    sx: {
                      maxWidth: "240px",
                      overflow: "hidden",
                      textOverflow: "ellipsis",
                      whiteSpace: "nowrap",
                    },
                  }}
                />
              </ListItem>
            ))}
          </List>
        </Paper>
      )}
    </Box>
  );
};

export default ResumeUpload;
