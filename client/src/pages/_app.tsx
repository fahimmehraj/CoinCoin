import NavigationBar from '../components/navbar'

import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <NavigationBar />
      <Component {...pageProps} />
    </>
  )
}

export default MyApp
