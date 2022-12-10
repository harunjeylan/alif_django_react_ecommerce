import { Box, Typography } from "@mui/material";
import { useTheme } from "@emotion/react";
import { tokens } from "../import";

function Footer() {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Box
      className="py-8 pt-[70px] mt-[70px] px-2 lg:px-4"
      backgroundColor={colors.primary[400]}
    >
      <Box className="w-full lg:w-[80%] mx-auto grid grid-cols-3lg:grid-cols-12 gap-1 lg:gap-8">
        <Box className="col-span-3  pb-4 lg:pb-0  lg:col-span-6">
          <Typography
            variant="h4"
            fontWeight="bold"
            className="mb-4 lg:mb-6"
            color={colors.greenAccent[500]}
          >
            ECOMMER
          </Typography>
          <div>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat
          </div>
        </Box>

        <Box className="col-span-1 lg:col-span-2 ">
          <Typography variant="h4" fontWeight="bold" className="mb-4 lg:mb-6">
            About Us
          </Typography>
          <Typography className="mb-4 lg:mb-6">Careers</Typography>
          <Typography className="mb-4 lg:mb-6">Our Stores</Typography>
          <Typography className="mb-4 lg:mb-6">Terms & Conditions</Typography>
          <Typography className="mb-4 lg:mb-6">Privacy Policy</Typography>
        </Box>

        <Box className="col-span-1 lg:col-span-2">
          <Typography variant="h4" fontWeight="bold" className="mb-4 lg:mb-6">
            Customer Care
          </Typography>
          <Typography className="mb-4 lg:mb-6">Help Center</Typography>
          <Typography className="mb-4 lg:mb-6">Track Your Order</Typography>
          <Typography className="mb-4 lg:mb-6">
            Corporate & Bulk Purchasing
          </Typography>
          <Typography className="mb-4 lg:mb-6">Returns & Refunds</Typography>
        </Box>

        <Box className="col-span-1 lg:col-span-2">
          <Typography variant="h4" fontWeight="bold" className="mb-4 lg:mb-6">
            Contact Us
          </Typography>
          <Typography className="mb-4 lg:mb-6">
            50 north Whatever Blvd, Washington, DC 10501
          </Typography>
          <Typography className="mb-4 lg:mb-6" sx={{ wordWrap: "break-word" }}>
            Email: mredwardroh@gmail.com
          </Typography>
          <Typography className="mb-4 lg:mb-6">(222)333-4444</Typography>
        </Box>
      </Box>
    </Box>
  );
}

export default Footer;
