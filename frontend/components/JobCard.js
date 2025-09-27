export default function JobCard({ title, company, location, url }) {
  return (
    <a href={url} target="_blank" rel="noopener noreferrer">
      <div className="p-4 border rounded shadow hover:shadow-lg transition">
        <h2 className="font-semibold text-xl">{title}</h2>
        <p className="text-gray-600">{company} — {location}</p>
      </div>
    </a>
  );
}
