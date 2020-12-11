/** @jsx jsx */
import { jsx } from "theme-ui"
import { Link } from "gatsby"

const Header = ({ siteTitle = `` }: { siteTitle: string }) => (
  <header
    sx={{
      variant: "styles.header",
    }}
  >
    <h1>
      <Link
        to="/"
        sx={{
          variant: "styles.navlink",
        }}
      >
        {siteTitle}
      </Link>
    </h1>
    <div sx={{ mx: "auto" }} />
    <Link
      to="https://github.com/okdyy75/freelance"
      sx={{
        variant: "styles.navlink",
      }}
    >
      GitHub
    </Link>
  </header>
)

export default Header
