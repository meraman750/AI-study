import { useState } from 'react';
import { QuestionInput } from './';
import { SubjectTabs } from './component/SubjectTabs';
import { SolutionCard } from './component/SolutionCard';
import { ExampleProblems } from './component/ExampleProblems';
import { Brain } from 'lucide-react';

export default function App() {
  const [activeSubject, setActiveSubject] = useState('all');
  const [solutions, setSolutions] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const generateMockSolution = (question) => {
    // ... (mock solution generation logic)
    return {
      id: Math.random().toString(36).substring(2, 9),
      question,
      answer: 'This is a mock answer',
      explanation: 'Step-by-step explanation goes here',
      steps: [
        { number: 1, title: 'Step 1', content: 'Do something' },
        { number: 2, title: 'Step 2', content: 'Do next thing' },
      ],
      subject: activeSubject,
    };
  };

  const handleQuestionSubmit = (question, image) => {
    setIsLoading(true);
    setTimeout(() => {
      const solution = generateMockSolution(question);
      setSolutions([solution, ...solutions]);
      setIsLoading(false);
    }, 1500);
  };

  return (
    <div className="min-h-screen bg-background">
      <header className="bg-white border-b border-border sticky top-0 z-10">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-purple-600 to-blue-600 rounded-lg flex items-center justify-center">
              <Brain className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1>AI Study Helper</h1>
              <p className="text-muted-foreground text-sm">
                Get instant solutions with step-by-step explanations
              </p>
            </div>
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-6 py-8">
        <div className="mb-6">
          <SubjectTabs activeSubject={activeSubject} onSubjectChange={setActiveSubject} />
        </div>

        <div className="mb-8">
          <QuestionInput onSubmit={handleQuestionSubmit} isLoading={isLoading} />
        </div>

        {solutions.length === 0 ? (
          <ExampleProblems onSelectExample={handleQuestionSubmit} />
        ) : (
          <div className="space-y-6">
            {solutions.map((solution) => (
              <SolutionCard key={solution.id} solution={solution} />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}