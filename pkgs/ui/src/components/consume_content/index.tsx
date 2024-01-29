const ConsumeDisplayComponent = ({ htmlContent }: { htmlContent: any }) => {
  return (
    <div>
      <div dangerouslySetInnerHTML={{ __html: htmlContent }} />
    </div>
  );
};

export default ConsumeDisplayComponent;
