/** @jsx jsx */
import { jsx, Flex, Text } from "theme-ui"
import * as React from "react"
import { Link, useStaticQuery, graphql } from "gatsby"

import Header from "../components/header"
import Image from "../components/image"
import "../styles/layout.css"

const Layout = ({ children }: { children: any }) => {
  const data = useStaticQuery(graphql`
    query SiteTitleQuery {
      site {
        siteMetadata {
          title
        }
      }
    }
  `)

  return (
    <>
      <Header siteTitle={data.site.siteMetadata?.title || `Title`} />
      <div
        sx={{
          variant: "styles.container",
        }}
      >
        <main>{children}</main>
        <footer
          sx={{
            variant: "styles.footer",
          }}
        >
          <div sx={{ mx: "auto" }} />

          <Text variant="p">
            {`© ${new Date().getFullYear()}, Built with`}
          </Text>

          <Link
            to="https://www.gatsbyjs.com"
            sx={{
              px: 2,
              variant: "styles.navlink",
            }}
          >
            <Flex>
              <Image path={`gatsby-icon.png`} width={24} height={24} />
              <div sx={{ px: 1 }}>Gatsby</div>
            </Flex>
          </Link>
        </footer>
      </div>
    </>
  )
}

export default Layout
