import React from "react"
import { Heading } from "theme-ui"
import { PageProps } from "gatsby"

import Layout from "../layouts/layout"
import SEO from "../components/seo"
import Levtech from "../components/levtech"

type PageContextProps = {
  site: string
}

const Site: React.FC<PageProps<object, PageContextProps>> = ({ pageContext }) => {
  const { site } = pageContext
  return (
    <Layout>
      <SEO title={site} />
      <Heading as="h1" variant="h1">
        {site}
      </Heading>
      {site === `Levtech` && <Levtech />}
    </Layout>
  )
}

export default Site
