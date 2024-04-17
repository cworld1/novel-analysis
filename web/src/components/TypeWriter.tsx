import { useState, useEffect } from "react";

interface TypewriterProps {
  children: React.ReactNode[];
  typingSpeed?: number;
}

const Typewriter: React.FC<TypewriterProps> = ({
  children,
  typingSpeed = 100,
}) => {
  const [displayText, setDisplayText] = useState("");
  const [nodeIndex, setNodeIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [typingCompleted, setTypingCompleted] = useState(false);

  useEffect(() => {
    if (!typingCompleted) {
      const node = children[nodeIndex];
      const text = (node as any).props.children;

      const timer = setTimeout(() => {
        setDisplayText((prev) => prev + text[charIndex]);

        if (charIndex < text.length - 1) {
          setCharIndex((prev) => prev + 1);
        } else if (nodeIndex < children.length - 1) {
          setDisplayText((prev) => prev + "<br/>");
          setNodeIndex((prev) => prev + 1);
          setCharIndex(0);
        } else {
          setTypingCompleted(true);
        }
      }, typingSpeed);

      return () => clearTimeout(timer);
    }
  }, [displayText, nodeIndex, charIndex, typingCompleted]);

  return <div dangerouslySetInnerHTML={{ __html: displayText }} />;
};

export default Typewriter;
