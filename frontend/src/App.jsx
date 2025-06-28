import ErrorBoundary from './components/ErrorBoundary'
import ConnectionStatus from './components/ConnectionStatus'
import GameBoard from './components/GameBoard'

function App() {
  return (
    <ErrorBoundary>
      <ConnectionStatus />
      <GameBoard />
    </ErrorBoundary>
  )
}

export default App